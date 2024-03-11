# Changeln

The application is designed to automate the generation of reports based on git history in the following formats:

* markdown
* html
* pdf

Comments with a specific format are used for generation,
Simply put, a comment that should be included in the report must have a tag.
For example:

```
[feature] My best commit.
```

Tags and groups can be defined in the configuration file. By default, there are 3 tags:

* `[bug]` - bug fix
* `[change]` - change of current feature
* `[feature]` - new feature

It is possible to customize the changelog file generation format using the [Mako](https://www.makotemplates.org/) template engine.

To start using the application, simply call it in the directory with your project,
the application will add the necessary configuration files and create changelog.md for you:

```shell
changeln
```

It is possible to specify the path to the configuration file,
This is convenient when one project requires several different readings.

By default, a file is generated in `markdown` format. To generate `pdf` you can call:

```shell
changeln --out pdf
```

And for the countdown in `html`:

```shell
changeln --out html
```

If you have an idea on how to improve applications or you encounter an error,
welcome to [GitHub](https://github.com/keygenqt/changeln).

And don't forget to put stars =)
