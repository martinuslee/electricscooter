import torch


model = torch.load(
    "/home/dkjh/datacampus/electricscooter/v5s_e300_best_0825.pt", map_location=torch.device("cpu")
)

torch.save(model, "cpu_model.pt")
