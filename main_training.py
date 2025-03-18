import os
import yaml
from nexa.training.load_data import load_data
from nexa.training.quantize_qat_convert import quantize_convert_model
from nexa.training.training import train_model

CONFIG = {}

# Load the config.yaml file
def load_yaml(config_file):
    """Load the configuration from a YAML file."""
    global CONFIG
    with open(config_file, 'r') as file:
        CONFIG = yaml.safe_load(file)
    return CONFIG

def prepare_iteration_directory(base_directory, sections, config_file):
    """Prepare directories and section configuration files."""
    section_lines = {section: [] for section in sections}
    current_section = None

    # Read the configuration file and organize lines by section
    with open(config_file, 'r') as file:
        for line in file:
            line_stripped = line.strip()
            if any(line_stripped.startswith(section + ":") for section in sections):
                current_section = line_stripped.split(":")[0]
            if current_section:
                section_lines[current_section].append(line)

    # Write section-specific configuration files
    for section, lines in section_lines.items():
        if lines:  
            os.makedirs(os.path.join(base_directory, section), exist_ok=True)
            file_path = os.path.join(base_directory, section, f"{section}_configs.txt")

            if not os.path.exists(file_path):
                with open(file_path, "w") as section_file:
                    section_file.writelines(lines)
                print(f"{file_path} created successfully.")
            else:
                print(f"{file_path} already exists. Skipping.")

def main():
    """Main execution function."""
    global CONFIG

    # Determine the iteration number
    list_folders = [int(item) for item in os.listdir('experiments') if item.isdigit()]
    iteration = max(list_folders) if list_folders else 0

    # Load the YAML configuration
    load_yaml("config.yaml")
    CONFIG['iteration'] = iteration

    # Prepare experiment directories
    base_directory = f"experiments/{iteration}"
    sections = ['preprocessing', 'training', 'post_processing']
    prepare_iteration_directory(base_directory, sections, "config.yaml")

    # Load datasets
    train_dataset, val_dataset, test_dataset = load_data(base_directory)

    # Train the model
    model = train_model(train_dataset, val_dataset, test_dataset, CONFIG)
    print(model.summary())

    # Quantize and convert the model
    quantize_convert_model(model, train_dataset, val_dataset, test_dataset, CONFIG)

# Entry point
if __name__ == "__main__":
    main()
