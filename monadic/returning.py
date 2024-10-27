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
        # Calculate average age
        avg_age = df.age.mean()

        # Find oldest user
        oldest_idx = df.age.idxmax()
        oldest_user = df.iloc[oldest_idx]

        # Count adults
        adult_count: int = (df.is_adult == True).sum()  # type: ignore

        summary = (
            f"Summary:\n"
            f"- Average age is {avg_age:.1f}\n"
            f"- Oldest user is {oldest_user.name} (ID: {oldest_user.id}) at age {oldest_user.age}\n"
            f"- Number of adults: {adult_count}"
        )
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
print("Testing with valid data:")
result_valid = process_user_data(valid=True)
match result_valid:
    case Success(value):
        print("Success:\n{}".format(value))
    case Failure(error):
        print("Error:", error)

print("\n---\n")

# Execute with invalid data
print("Testing with invalid data:")
result_invalid = process_user_data(valid=False)
match result_invalid:
    case Success(value):
        print("Success:\n{}".format(value))
    case Failure(error):
        print("Error:", error)
