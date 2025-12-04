import kagglehub
import os
def main():
  # Download latest version
  path = kagglehub.dataset_download("solarmainframe/ids-intrusion-csv")
  
  print("Path to dataset files:", path)
  
  
  df_list = []
  
  # Process files from /kaggle/input/ids-intrusion-csv/
  if os.path.exists('/kaggle/input/ids-intrusion-csv/'):
      for file in os.listdir('/kaggle/input/ids-intrusion-csv/'):
          file_path = os.path.join('/kaggle/input/ids-intrusion-csv/',file)
          if os.path.isfile(file_path):
              # Read the CSV in chunks to reduce memory usage
              print('/kaggle/input/ids-intrusion-csv/', file)
              for chunk in pd.read_csv(file_path, chunksize=10000,low_memory=False):
                  # Sample a fraction of each chunk
                  df_list.append(chunk.sample(frac=0.1, random_state=RANDOM_SEED))
  
  df = pd.concat(df_list, ignore_index=True)
  print(df.shape)
