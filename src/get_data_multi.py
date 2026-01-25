import yfinance as yf
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, '..', 'data')
os.makedirs(DATA_DIR, exist_ok=True)

def download_data_multivariable():

    tickers = ['CLP=X', 'HG=F', 'DX=F', 'CNY=X']
    df = yf.download(tickers, period='max', interval='1d')

    if len(df) > 0:
        print(f"se descargaron en total {len(df)} filas.")
    else:
        print("no se descargaron datos")
        return

    df = df['Close']

    #dropna para eliminar filas con datos faltantes, al ser para multiariable todas la filas deben tener datos
    #ffill para llenar datos faltantes con datos de mas adelante
    df = df.ffill().dropna() #combinar las dos para disminuir filas nulas

    df = df.rename(columns={
        'CLP=X': 'CLP',         # target 
        'HG=F':  'Cobre',       # Feature
        'DX=F':  'Dolar_Index', # Feature
        'CNY=X': 'Yuan'         # Feature
    })

    file_path = os.path.join(DATA_DIR, 'clp_multivariable.csv')
    df.to_csv(file_path)
    
    print(f"dataset guardado en: {file_path}")
    print(f"dimensiones finales: {df.shape}")
    print(f"variables {list(df.columns)}")

if __name__ == "__main__":
    download_data_multivariable()