import kagglehub
import os
import pandas as pd

RANDOM_SEED = 42  # use o valor que quiser

def main():
    print("Start")

    # Baixa (ou reutiliza cache) do dataset
    path = kagglehub.dataset_download("solarmainframe/ids-intrusion-csv")
    print("Path to dataset files:", path)

    # Use o caminho retornado pelo kagglehub
    base_path = path
    print("Lendo arquivos de:", base_path)

    df_list = []

    if os.path.exists(base_path):
        # Caminhar por todas as subpastas, se existirem
        for root, dirs, files in os.walk(base_path):
            for file in files:
                file_path = os.path.join(root, file)
                if os.path.isfile(file_path) and file_path.endswith(".csv"):
                    print("Lendo:", file_path)
                    # Lê em chunks para economizar memória
                    for chunk in pd.read_csv(file_path, chunksize=10000, low_memory=False):
                        # Amostra 10% de cada chunk
                        df_list.append(chunk.sample(frac=0.1, random_state=RANDOM_SEED))
    else:
        print("Pasta não encontrada:", base_path)
        return

    if not df_list:
        print("Nenhum CSV carregado, df_list está vazio.")
        return

    df = pd.concat(df_list, ignore_index=True)
    print("Shape final:", df.shape)

    # Se quiser salvar o resultado amostrado:
    out_path = "data/CSE-CIC-IDS2018/CSE-CIC-IDS2018_sample.csv"
    df.to_csv(out_path, index=False)
    print(f"Arquivo salvo em: {out_path}")

    return df

if __name__ == "__main__":
    main()
