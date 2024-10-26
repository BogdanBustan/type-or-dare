from dataclasses import dataclass, field
from typing import List, Dict, Optional
from datetime import datetime


# Simple dataclass with immutable defaults
@dataclass
class User:
    name: str  # Required field (no default)
    email: str  # Required field (no default)
    age: int = 18  # Optional with default value
    is_active: bool = True  # Optional with default value


# Frozen dataclass (immutable)
@dataclass(frozen=True)
class Configuration:
    api_key: str  # Required field
    host: str = "localhost"  # Optional with default
    port: int = 8080  # Optional with default
    debug: bool = False  # Optional with default


# Dataclass with mutable defaults
@dataclass
class BlogPost:
    # Required fields first
    title: str
    content: str

    # Mutable defaults must use default_factory
    tags: List[str] = field(default_factory=list)
    metadata: Dict[str, str] = field(default_factory=dict)

    # Immutable defaults can use direct assignment
    views: int = 0
    created_at: datetime = field(default_factory=datetime.now)


def demonstrate_usage():
    # Basic usage
    user = User(
        name="Alice",
        email="alice@example.com"
        # age and is_active will use defaults
    )
    print(user)  # User(name='Alice', email='alice@example.com', age=18, is_active=True)

    # Frozen dataclass
    config = Configuration(api_key="secret123")
    print(config)  # Configuration(api_key='secret123', host='localhost', port=8080, debug=False)
    # config.port = 9000  # This would raise FrozenInstanceError

    # Mutable defaults
    post = BlogPost("My Title", "My Content")
    post.tags.append("python")
    post.metadata["author"] = "Alice"
    print(post)

    # Each instance gets its own copy of mutable defaults
    post2 = BlogPost("Another Title", "More Content")
    print(post2.tags)  # []
    print(post.tags)  # ['python']


if __name__ == "__main__":
    demonstrate_usage()