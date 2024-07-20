# Gemstone Price Predictor

You are hired by a company Gem Stones Co Ltd. You are provided with the dataset containing the prices and other attributes of almost 27,000 cubic gemstone. The company is earning different profits on different prize slots. You have to help the company in predicting the price for the stone on the basis of the details given in the dataset so it can distinguish between higher profitable stones and lower profitable stones so as to have a better profit share. Also, provide them with the best 5 attributes that are most important.

## Demo

![gem](https://github.com/thanseefpp/Gemstone-Price-Prediction/assets/62167887/8bdb312a-4da0-4f26-99af-c156c4544060)



## Data Features
- **Carat**: Carat weight of the gemstone.
- **Cut**: Describe the cut quality of the gemstone. Quality is increasing order: Fair, Good, Very Good, Premium, Ideal.
- **Color**: Color of the gemstone. With D being the best and J the worst.
- **Clarity**: Gemstone clarity refers to the absence of inclusions and blemishes. (In order from best to worst: FL = flawless, I3 = level 3 inclusions) FL, IF, VVS1, VVS2, VS1, VS2, SI1, SI2, I1, I2, I3.
- **Depth**: The height of a gemstone, measured from the culet to the table, divided by its average girdle diameter.
- **Table**: The width of the gemstone's table expressed as a percentage of its average diameter.
- **Price**: The price of the gemstone.
- **X**: Length of the gemstone in mm.
- **Y**: Width of the gemstone in mm.
- **Z**: Height of the gemstone in mm.

## Create project template hierarchy



```bash
  python template.py
```


## Setup development environment
```bash
  bash init_setup.sh
```
## Activate environment
```bash
  source activate env/
```


## Install project as local package
```bash
  pip install -r requirement.txt
```
## Flask App
```bash
  python run app.py
```
