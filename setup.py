from setuptools import setup, find_packages

setup(
    name="mcp-ponder-tool",
    version="0.1.0",
    description="An MCP server implementing the ponder tool for Claude and other LLMs",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/mcp-ponder-tool",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "mcp>=1.2.0",
    ],
    python_requires=">=3.10",
    entry_points={
        "console_scripts": [
            "mcp-ponder-tool=ponder_tool.server:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
    ],
)