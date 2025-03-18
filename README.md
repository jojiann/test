# Workflow for Transforming EDF Files and Training an Akida Model

This workflow outlines the process for transforming EEG data from EDF files into 3D STFT representations and then training a model using the Akida engine. The workflow consists of two main scripts: `main.py` for data transformation and `main_training.py` for model training. The configuration file, `config.yaml`, can be edited to customize parameters for the data processing and training.

## Prerequisites
- Python environment with required libraries installed
- `config.yaml` file for customizing workflow settings
- Access to EDF files for EEG data (all EDF files should be in a folder called EDFs)
- Akida SDK for model deployment

## Steps

### 1. **Configure `config.yaml` File**
The `config.yaml` file contains various parameters that can be edited to modify how the data is processed and the training is performed. You can modify the following settings in the config file:
- **Low and High Filters**: Set the frequency range for band-pass filtering.
- **Segments**: Define the segment length for data preprocessing.
- **Stimulation Type**: Specify the type of stimulation to be applied to the data.
- **Number of Epochs**: Define the number of epochs for model training.
- **Normalization Type**: Select the type of normalization to be applied to the data (e.g., MinMax, Z-score).
- **3rd STFT Layer**: Choose the method to calculate the third STFT layer (e.g., magnitude, phase).

```yaml
processing:
  low_filter: 0.1  # Low filter frequency in Hz
  high_filter: 50.0  # High filter frequency in Hz
  segment_duration: 30  # Duration of segments in seconds
  stacking: True  # Whether to stack the data
  stimulation_type: 'Bipolar'  # Stimulation type
  3rd_stft_method: 'magnitude'  # STFT method (magnitude, phase, etc.)

training:
  epochs: 50  # Number of epochs for training
  normalization: 'z-score'  # Normalization type (MinMax, Z-score, etc.)
```

### 2. **Run Data Transformation with `main.py`**

The first script, `main.py`, is responsible for transforming the EEG data into 3D STFT arrays. The script takes EDF files, applies preprocessing (such as filtering and segmentation), and generates stacked STFT arrays, ready for model training.

**Key Actions** in `main.py`:

- **Load EDF Files**: Read EEG data from EDF files.
- **Filter Data**: Apply low-pass and high-pass filters to the data according to the parameters in `config.yaml`.
- **Segment Data**: Divide the data into segments as specified in the configuration file.
- **Generate STFT**: Compute the Short-Time Fourier Transform (STFT) for each segment.
- **Stack STFT Layers**: Optionally, stack the STFT layers as specified in the configuration file.

**Command to run** `main.py`:

```
python main.py

```

### 3. **Train the Model with** `main_training.py`
Once the data has been preprocessed and transformed into 3D STFT arrays, the second script, `main_training.py`, is used to initiate model training. This script will use the transformed data from the previous step to train an Akida model.

**Key Actions** in `main_training.py`:

- **Load Transformed Data**: Read the preprocessed 3D STFT data.
- **Normalize Data**: Apply the selected normalization method (e.g., z-score normalization).
- **Train Model**: Train the model using the specified number of epochs and the Akida engine.
- **Save Model**: After training, the model is saved for future use or deployment.

**Command to run** `main_training.py`:
```
python main_training.py

```

### 4. Model Deployment
Once the model is trained, you can deploy it using Akida's deployment tools. The model can be converted to a format compatible with the Akida engine for inference on embedded devices or other platforms.

### Example Workflow in Action
1. Edit the `config.yaml` file to configure preprocessing and training parameters.
2. Run `main.py` to transform the raw EDF data into 3D STFT representations.
3. Run `main_training.py` to train the Akida model using the processed data.
4. Once training is complete, deploy the trained model using the Akida tools.

## Conclusion
This workflow provides a step-by-step guide for preprocessing EEG data, generating 3D STFT representations, and training an Akida model. By editing the config.yaml file, you can customize the preprocessing and training steps to suit your specific needs. Ensure to run each script separately in the correct order for successful model training and deployment.

# Steps of creating a `pip` package
Make sure that you are in the main directory in your terminal.
### 1. Run `python setup.py sdist bdist_wheel`
### 2. Then this `pip install dist/nexa-0.1.0.tar.gz`

You should then see a build and a dist files with nexa.egg-info folder. And now you are all set to import your packages! 
