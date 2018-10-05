# Modularized configuration files

[![](https://gitlab.klitzke-web.de/lkl/pymodconf/badges/master/pipeline.svg)](https://gitlab.klitzke-web.de/lkl/pymodconf/tree/master)

This is a Python package which enables to modularize configuration files.

In configuration-based applications, it is sometimes desirable to group
sections in a configuration file. This can, for instance, be sections which are for a specific purpose, e.g. modules in
an application which shall be configurable.

For this purpose, `pymodconf` add the functionality to define custom `Tag`s representing groups in a configuration file.
For instance, if you have an application with multiple modules you can define the tag `Module:` and add that prefix to
each section in the configuration file describing a certain module.

## Installation

You can find the latest version on [PyPi](https://pypi.org/project/pymodconf/). So simply use `pip` with

```bash
pip install pymodconf
```

## Usage

This following configuration file shows the feature set of `pymodconf`:

```ini
1: [Application]
2: name=pymodconf
3: string=Hello ${name}!
4: list=One, Two, Three, Four

6: [Some Section]
7: opt=${Application:name}-section

9: [Module: Test]
10:log-dir= /tmp/test_module
```

### Sections

In line `[1]`  a new section `Application` is created with multiple options show in lines `[2]-[3]`.

### Variable replacement

Due to the fact that `pymodconf` is based on the `configparser` module, the variable-replacement feature is available,
too. In line `[3]` a reference to an option in the same section is shown. If you want to reference an option in any
other section, you'll have to specify the name of the section, as you can see in line `[7]`.

### Lists

If `pymodconf` finds any commata in the value of an option, it will split up that value and generate a list of it. In
line `[4]` the value is represented in Python as a list with four entries: 'One', 'Two', 'Three', 'Four'.

### Directory creation

Another feature of `pymodconf` is the automatic directory creation. If any option name ends with the suffix `-dir` it
will try to recursively create the directory tree. For instance, due to the definition in line `[10]`, a directory
`test-module` will be created in the directory `/tmp/`.

### Tagging

The most interesting feature of `pymodconf` is the ability to group sections using user-defined `Tag`s. As you can see
in line `[9]` a section with the tag definition `Module` is defined.

Before `pymodconf` is able to group such sections, you'll have to register the tag ad `pymodconf` with:

```python
import pymodconf as mc

module_tag = mc.tag.Tag('Module:')
mc.tag.register(module_tag)
```

Afterwards, you can load the configuration file with:

```python
config = mc.parser.load('example.cfg')
```

The result is dictionary with section names and user-defined modules as keys and the corresponding options as values.

## Thanks

If you like this tool, donate some bugs 💸 for a drink or two at the ETH-Wallet
*0xf7d518A730D93a6d27415EcaE5D801Dde125dE15*,
XRP-Wallet *rhVWrjB9EGDeK4zuJ1x2KXSjjSpsDQSaU6* with destination tag *653103618* or via
[PayPal](https://www.paypal.me/LarsKlitzke). Cheers 🍻!

## License

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the
implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
details.

You should have received a copy of the GNU General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.

