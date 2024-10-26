from typing import TypedDict, List


# Basic TypedDict
class UserProfile(TypedDict):
    name: str
    age: int
    email: str


# Usage
user: UserProfile = {
    "name": "Alice",
    "age": 30,
    "email": "alice@example.com"
}


# TypedDict with optional fields
class BlogPost(TypedDict, total=False):  # total=False makes all fields optional
    title: str
    content: str
    tags: List[str]
    views: int
    author: str


# Fields 'views' and 'tags' can be omitted
post: BlogPost = {
    "title": "Python Types",
    "content": "TypedDict is useful...",
    "author": "Alice"
}


# Nested TypedDict
class Address(TypedDict):
    street: str
    city: str
    country: str
    postal_code: str


class Employee(TypedDict):
    name: str
    position: str
    address: Address
    skills: List[str]


# Using nested TypedDict
employee: Employee = {
    "name": "Bob Smith",
    "position": "Developer",
    "address": {
        "street": "123 Main St",
        "city": "Boston",
        "country": "USA",
        "postal_code": "02101"
    },
    "skills": ["Python", "TypeScript", "Docker"]
}


# TypedDict inheritance
class BaseConfig(TypedDict):
    app_name: str
    version: str


class FullConfig(BaseConfig):
    debug: bool
    api_key: str


# Using inherited TypedDict
config: FullConfig = {
    "app_name": "MyApp",
    "version": "1.0.0",
    "debug": True,
    "api_key": "secret123"
}
