import wandb

def init_wandb(project_name, config_dict):

    # initilize wandb logging
    wandb.init(project=project_name, config=config_dict)
    return wandb.config
