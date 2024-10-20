from typing import Any, cast, Union
import pandas as pd
import pandera as pa
from pandera.typing import DataFrame, Series
from returns.result import Result, Success, Failure
from returns.pipeline import is_successful


# Define a custom error type that can represent both SchemaError and Exception
class ProcessingError(Exception):
    pass


# Define a Pandera schema for validation using DataFrameModel
class UserSchema(pa.DataFrameModel):
    id: Series[int]
    name: Series[str]
    age: Series[int]

    class Config:
        strict = True  # Disallow unknown columns


# Function to generate sample data
def generate_data(valid: bool = True) -> pd.DataFrame:
    if valid:
        data = {
            "id": [1, 2, 3],
            "name": ["Alice", "Bob", "Charlie"],
            "age": [25, 30, 35],
        }
    else:
        # Introduce an error: 'age' has a string instead of int
        data = {
            "id": [1, 2, 3],
            "name": ["Alice", "Bob", "Charlie"],
            "age": [25, "thirty", 35],
        }
    return pd.DataFrame(data)


# Function to validate data
def validate_data(df: pd.DataFrame) -> Result[DataFrame[UserSchema], ProcessingError]:
    try:
        validated_df = UserSchema.validate(df)
        validated_df = cast(DataFrame[UserSchema], validated_df)
        return Success(validated_df)
    except pa.errors.SchemaError as e:
        return Failure(ProcessingError(str(e)))


# Function to transform data: add a new column 'is_adult'
def add_is_adult(df: DataFrame[UserSchema]) -> Result[DataFrame[UserSchema], ProcessingError]:
    try:
        df_with_adult = df.assign(is_adult=df.age >= 18)
        return Success(df_with_adult)
    except Exception as e:
        return Failure(ProcessingError(str(e)))


# Function to summarize data
def summarize_data(df: DataFrame[UserSchema]) -> Result[str, ProcessingError]:
    try:
        average_age = df.age.mean()
        summary = f"Average age is {average_age}"
        return Success(summary)
    except Exception as e:
        return Failure(ProcessingError(str(e)))


# Main processing function using monadic chaining
def process_user_data(valid: bool = True) -> Result[str, ProcessingError]:
    data = generate_data(valid)
    return (
        validate_data(data)
        .bind(add_is_adult)
        .bind(summarize_data)
    )


# Execute with valid data
result_valid = process_user_data(valid=True)
if is_successful(result_valid):
    print("Success:", result_valid.unwrap())
else:
    print("Validation Error:", result_valid.failure())

# Execute with invalid data
result_invalid = process_user_data(valid=False)
if is_successful(result_invalid):
    print("Success:", result_invalid.unwrap())
else:
    print("Validation Error:", result_invalid.failure())
