import kagglehub

# Download latest version
path = kagglehub.model_download("google/movenet/tensorFlow2/multipose-lightning")

print("Path to model files:", path)