# AgriTech
An app with deep learning model to predict compatibility using soil images and also assists in minimising loss at harvest time by predicting prices.
Developed at IndiaHacks 2017

## Requirements
1. Beautiful Soup
2. Tensorflow
3. Numpy
4. Pandas

## How To Use
1. First scrape crop prices data from agmarknet.gov.in using python web scraping website beautiful soup.
```
python scrap_crops.py
```
This will give output csv file for different states, crops and over different months.

2. To predict prices of crops after harvesting period, run
```
python ./scripts/hack1.py
```
This uses a random forest regressor to predict prices.


3. Train an inceptionv3 model inn tensorflow using transfer learning to classify soil type by image.
```
python ./scripts/retrain.py --imagedir <pathtoimages>
```
4. Complete pipeline output\\
Get best crop to grow from soil image taking into consideration price prediction after harvest time.
```
python ./scripts/label_image.py
```
