<h1 align="center" style="margin-top: 0px;">{{ cookiecutter.name | lower }}</h1>

<p align="center">
<a href="https://github.com/space-code/{{ cookiecutter.name | lower }}/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/github/license/space-code/{{ cookiecutter.name | lower }}?style=flat"></a> 
<a href="https://developer.apple.com/swift"><img alt="{{ cookiecutter.swift_version }}" src="https://img.shields.io/badge/language-Swift{{ cookiecutter.swift_version }}-orange.svg"/></a>
<a href="https://github.com/space-code/{{ cookiecutter.name | lower }}"><img alt="CI" src="https://github.com/space-code/{{ cookiecutter.name }}/actions/workflows/ci.yml/badge.svg?branch=main"></a>
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
Nikita Vasilev, nv3212@gmail.com

## License
{{ cookiecutter.name | lower }} is available under the MIT license. See the LICENSE file for more info.