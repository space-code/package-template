<h1 align="center" style="margin-top: 0px;">{{ cookiecutter.name | lower }}</h1>

<p align="center">
<a href="https://github.com/space-code/{{ cookiecutter.name | lower }}/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/github/license/space-code/{{ cookiecutter.name | lower }}?style=flat"></a> 
<a href="https://swiftpackageindex.com/space-code/{{ cookiecutter.name | lower }}"><img alt="Swift Compatibility" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fswiftpackageindex.com%2Fapi%2Fpackages%2Fspace-code%2F{{ cookiecutter.name | lower }}%2Fbadge%3Ftype%3Dswift-versions"/></a> 
<a href="https://swiftpackageindex.com/space-code/{{ cookiecutter.name | lower }}"><img alt="Platform Compatibility" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fswiftpackageindex.com%2Fapi%2Fpackages%2Fspace-code%2F{{ cookiecutter.name | lower }}%2Fbadge%3Ftype%3Dplatforms"/></a> 
<a href="https://github.com/space-code/{{ cookiecutter.name | lower }}"><img alt="CI" src="https://github.com/space-code/{{ cookiecutter.name }}/actions/workflows/ci.yml/badge.svg?branch=main"></a>
{% if cookiecutter.ios == "Yes" %}
<a href="https://github.com/space-code/{{ cookiecutter.name | lower }}"><img alt="Number of GitHub contributors" src="https://img.shields.io/github/issues/space-code/{{ cookiecutter.name | lower }}"></a>
<a href="https://github.com/space-code/{{ cookiecutter.name | lower }}"><img alt="Number of GitHub issues that are open" src="https://img.shields.io/github/stars/space-code/{{ cookiecutter.name | lower }}"></a>
<a href="https://github.com/space-code/{{ cookiecutter.name | lower }}"><img alt="Number of GitHub closed issues" src="https://img.shields.io/github/issues-closed/space-code/{{ cookiecutter.name | lower }}"></a>
<a href="https://github.com/space-code/{{ cookiecutter.name | lower }}"><img alt="Number of GitHub stars" src="https://img.shields.io/github/contributors/space-code/{{ cookiecutter.name | lower }}"></a>
<a href="https://github.com/space-code/{{ cookiecutter.name | lower }}"><img alt="Number of GitHub pull requests that are open" src="https://img.shields.io/github/issues-pr-raw/space-code/{{ cookiecutter.name | lower }}"></a>
{% endif %}
<a href="https://github.com/space-code/{{ cookiecutter.name | lower }}"><img alt="GitHub release; latest by date" src="https://img.shields.io/github/v/release/space-code/{{ cookiecutter.name | lower }}"></a>
<a href="https://github.com/apple/swift-package-manager" alt="{{ cookiecutter.name | lower }} on Swift Package Manager" title="{{ cookiecutter.name | lower }} on Swift Package Manager"><img src="https://img.shields.io/badge/Swift%20Package%20Manager-compatible-brightgreen.svg" /></a>
</p>

## Description
`{{ cookiecutter.name }}` description.

- [Usage](#usage)
- [Requirements](#requirements)
- [Installation](#installation)
- [Communication](#communication)
- [Contributing](#contributing)
- [Author](#author)
- [License](#license)

## Usage

## Requirements

## Installation
### Swift Package Manager

The [Swift Package Manager](https://swift.org/package-manager/) is a tool for automating the distribution of Swift code and is integrated into the `swift` compiler. It is in early development, but `{{ cookiecutter.name | lower }}` does support its use on supported platforms.

Once you have your Swift package set up, adding `{{ cookiecutter.name | lower }}` as a dependency is as easy as adding it to the `dependencies` value of your `Package.swift`.

```swift
dependencies: [
    .package(url: "https://github.com/space-code/{{ cookiecutter.name | lower }}.git", .upToNextMajor(from: "{{ cookiecutter.package_version }}"))
]
```

## Communication
- If you **found a bug**, open an issue.
- If you **have a feature request**, open an issue.
- If you **want to contribute**, submit a pull request.

## Contributing
Bootstrapping development environment

```
make bootstrap
```

Please feel free to help out with this project! If you see something that could be made better or want a new feature, open up an issue or send a Pull Request!

## Author
{{ cookiecutter.author }}, {{ cookiecutter.email }}

## License
{{ cookiecutter.name | lower }} is available under the MIT license. See the LICENSE file for more info.