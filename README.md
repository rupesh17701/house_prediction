# House Price Prediction

A Streamlit app that estimates house price (in ₹) from a Random Forest regression model trained on the classic Kaggle "Housing Prices" dataset.

## What it does

Enter area, bedroom/bathroom/story counts, parking spots, and a handful of yes/no amenities (main road access, guest room, basement, hot water heating, air conditioning, preferred area), and the app predicts a price using a pre-trained `RandomForestRegressor`.

## Run it locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Files

- `app.py` — Streamlit UI and inference
- `house_model.pkl` — trained RandomForestRegressor
- `columns.pkl` — the exact feature column order the model expects

## Tech stack

Python, Streamlit, scikit-learn, joblib, pandas.

## Known limitation

The trained model was fit on features that include `furnishingstatus` (semi-furnished / unfurnished, one-hot encoded), but the current UI never asks the user for furnishing status — those columns are silently filled with 0 (i.e. every prediction assumes the "furnished" baseline). Predictions for semi-furnished or unfurnished homes will be less accurate until the UI is extended to collect that input.
