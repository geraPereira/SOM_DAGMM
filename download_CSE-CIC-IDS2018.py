import os
import pandas as pd

RANDOM_SEED = 42  # ou o valor que você quiser

def main():
    print("Start")

    base_path = "/kaggle/input/ids-intrusion-csv"
    print("Lendo arquivos de:", base_path)

    df_list = []

    if os.path.exists(base_path):
        for file in os.listdir(base_path):
            file_path = os.path.join(base_path, file)
            if os.path.isfile(file_path) and file_path.endswith(".csv"):
                print("Lendo:", file_path)
                # Lê em chunks para economizar memória
                for chunk in pd.read_csv(file_path, chunksize=10000, low_memory=False):
                    df_list.append(chunk.sample(frac=0.1, random_state=RANDOM_SEED))
    else:
        print("Pasta não encontrada:", base_path)
        return

    if not df_list:
        print("Nenhum CSV carregado, df_list está vazio.")
        return

    df = pd.concat(df_list, ignore_index=True)
    print("Shape final:", df.shape)
    return df

if __name__ == "__main__":
    df = main()
