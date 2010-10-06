#!/bin/bash

#/usr/share/inkscape/extensions/layer2png.py -d img -l slices img/drawing.svg
/home/matt/work/inkscape/slicer/layer2png.py -o -d img -l slices img/drawing.svg

ODP=~/work/pylibs/docutilsSandbox/rst2odp/
PATH=$PATH:${ODP}bin
echo $PATH
#PYTHONPATH=${ODP} rst2odp.py --traceback -r 3 --mono-font "Commodore 64" --template-file templates/whitekids.otp week1.rst week1.odp
PYTHONPATH=${ODP} rst2odp.py --traceback -r 3 --mono-font "Envy Code R" --template-file templates/white.otp fullmeal.rst PythonFullMead.odp

# build handout
rst2odt.py -g --add-syntax-highlighting --stylesheet=templates/3coltemp.odt handout.rst FullMealHandout.odt 

for file in eat/*.py
do
  file=$(basename ${file})
  echo ${file}
  python ../MealMaker/mealmakerlib/__init__.py eat/${file} meals/${file}
done
