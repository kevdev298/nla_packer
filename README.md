# Simple NLA Packer

This is a simple NLA packer for [Blender](https://www.blender.org) for animation export with the [Godot Engine](https://godotengine.org).

## Installation
1. Copy automation_nla_packer directory into the scripts/addons directory where Blender is installed.
2. Go to Preferences -> Add-ons and enable the add-on in blender.

## How to use
This add on will allow quick and easy packing of all animations within a file for whatever armature you have selected.
1. Select the target armature
2. Open Automation Panel
3. Select "Pack Actions as NLA Tracks"

Animations should now packed in a manner that Godot can import when use with a compatible export format. Compatible formats can be found [here](https://docs.godotengine.org/en/stable/getting_started/workflow/assets/importing_scenes.html).

## Future Development
The ability to select specific animations to pack.

*If you find any bugs or want to suggest improvement, please open an issue on the repository.*

## License
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.