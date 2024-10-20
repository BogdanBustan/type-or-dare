from result import Result, Ok, Err
import pandera as pa
from pandera.typing import DataFrame, Series
import pandas as pd
from typing import Any, cast


# Define a Pandera schema for validation
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
def validate_data(df: pd.DataFrame) -> Result[DataFrame[UserSchema], pa.errors.SchemaError]:
    try:
        validated_df = UserSchema.validate(df)
        validated_df = cast(DataFrame[UserSchema], validated_df)
        return Ok(validated_df)
    except pa.errors.SchemaError as e:
        return Err(e)


# Function to transform data: add a new column 'is_adult'
def add_is_adult(df: DataFrame[UserSchema]) -> Result[DataFrame[UserSchema], Exception]:
    try:
        df = df.assign(is_adult=df.age >= 18)
        return Ok(df)
    except Exception as e:
        return Err(e)


# Function to summarize data
def summarize_data(df: DataFrame[UserSchema]) -> Result[str, Exception]:
    try:
        average_age = df.age.mean()
        summary = f"Average age is {average_age}"
        return Ok(summary)
    except Exception as e:
        return Err(e)


# Main processing function using monadic chaining
def process_user_data(valid: bool = True) -> Result[str, Any]:
    data = generate_data(valid)
    return (
        validate_data(data)
        .and_then(add_is_adult)
        .and_then(summarize_data)
    )


# Execute with valid data
result_valid = process_user_data(valid=True)
match result_valid:
    case Ok(value):
        print("Success:", value)
    case Err(error):
        print("Validation Error:", error)

# Execute with invalid data
result_invalid = process_user_data(valid=False)
match result_invalid:
    case Ok(value):
        print("Success:", value)
    case Err(error):
        print("Validation Error:", error)
