from nexa.edf_operations.main_edf import process_edf_folder

from nexa.stft_operations.generate_stft import generate_stft
import json
import os
import tensorflow as tf

from nexa.training.main_training import train_evaluate_convert


from nexa.visualization.visualize_stft_means import process_and_visualize_data


with open("config.json", "r") as file:
    config = json.load(file)


# Main function to run the entire pipeline
def main(edf_folder_path, config):
  
    # Processing EDF Files
    processed_data_dict = process_edf_folder(edf_folder_path, config)
    train_dataset, val_dataset, test_dataset = generate_stft(processed_data_dict, config)
    model, evaluation_results, akida_model, akida_evaluation_results  = train_evaluate_convert(train_dataset, val_dataset, test_dataset, config)

       
   

    print("\n✅ Full Pipeline Completed Successfully!")
    return model, evaluation_results, akida_model, akida_evaluation_results  
# Entry point
if __name__ == "__main__":
    main()
