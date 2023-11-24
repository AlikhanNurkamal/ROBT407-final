from torchinfo import summary
import torch
from models.vit import ViT_Ti_32


inp = torch.randn(1, 3, 224, 224)

vit = ViT_Ti_32()

print(vit(inp))

summary(model=vit,
        input_size=(32, 3, 224, 224),
        col_names=["input_size", "output_size", "num_params", "trainable"],
        col_width=20,
        row_settings=["var_names"]
)