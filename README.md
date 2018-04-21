# Localization using WiFi scans and Neural Net


## Requirements
- PyTorch
- Python-Iwlist


## Instructions


### Training Phase
A scanning phase has to be performed for each different zone.

That is done by running (should be done with root privileges for better results):

```python scanZone.py ZONE_NAME NUMBER_OF_SAMPLE```

This shoud generate a different json file for each zone.


### Merge the training data into a single dataset
That is done by running:

```python mergeDataset.py <zone1.json zone2.json ... >```

This creates the ```raw_dataset.json``` files


### Create support files
Run the following commands:

```python getAllAP.py```

```python getAllZones.py```

These generates ```aplist.json``` and ```zonelist.json```


### Train the neural network
That is done by running:

```python trainNet.py```


### Localize yourself
```bash localize.sh```
