if __name__ == '__main__':
    import os
    import numpy as np
    import torch

    from config import cfg
    # from trainer import Trainer
    # from trainer_CMTL import Trainer_CMTL
    #------------prepare environment------------
    seed = cfg.SEED
    if seed is not None:
        np.random.seed(seed)
        torch.manual_seed(seed)
        torch.cuda.manual_seed(seed)

    gpus = cfg.GPU_ID
    if len(gpus) == 1:
        torch.cuda.set_device(gpus[0])

    torch.backends.cudnn.benchmark = True

    #------------prepare data loader------------
    data_mode = cfg.DATASET
    if data_mode == 'SHHA':
        from datasets.SHHA.loading_data import loading_data 
        from datasets.SHHA.setting import cfg_data 
    elif data_mode == 'SHHB':
        from datasets.SHHB.loading_data import loading_data 
        from datasets.SHHB.setting import cfg_data 
    elif data_mode == 'QNRF':
        from datasets.QNRF.loading_data import loading_data 
        from datasets.QNRF.setting import cfg_data 
    elif data_mode == 'UCF50':
        from datasets.UCF50.loading_data import loading_data 
        from datasets.UCF50.setting import cfg_data 
    elif data_mode == 'WE':
        from datasets.WE.loading_data import loading_data 
        from datasets.WE.setting import cfg_data 
    elif data_mode == 'GCC':
        from datasets.GCC.loading_data import loading_data
        from datasets.GCC.setting import cfg_data 

    #------------Prepare Trainer------------
    net = cfg.NET
    from trainer import Trainer

    #------------Start Training------------
    pwd = os.path.split(os.path.realpath(__file__))[0]
    cc_trainer = Trainer(loading_data, cfg_data, pwd)
    cc_trainer.forward()
