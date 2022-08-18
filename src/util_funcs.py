from datetime import datetime
import getpass as gp
import time as t
import os





def get_user() -> str:
    """
    Get the user name of the current user
    
    :param system: The system obained by platform.system()
    :type system:  str
    :return:       The name of the user.
    """
    try:
        ret = gp.getuser()
    except:
        try:
            temp_list = os.getcwd().split(os.path.sep)
            ret = temp_list[ temp_list.index('Users') + 1 ]
        except:
            try:
                temp_list = __file__.split(os.path.sep)
                ret = temp_list[ temp_list.index('Users') + 1 ]
            except:
                ret = 'Unable to determine'
    return ret





def get_config_dir(system:str, usr:str, args) -> tuple:
    """
    Get the config directory & path to the config file
    
    :param system: The operating system
    :type system:  str
    :param usr:    The username of the current user
    :type usr:     str
    :return:       A tuple containing the config directory, config file path, and data directory
    """
    if system == 'Windows':
        # Local Appdata folder
        APPDATA    = os.environ['LOCALAPPDATA']
        APPDATA    = os.path.join('C:\\' , 'Users' , usr , 'AppData' , 'LOCAL') if not APPDATA else APPDATA
        # Config directory
        CONFIG_DIR = os.path.join(APPDATA, 'markify')
        # COnfig file
        CONFIG_FP  = os.path.join(CONFIG_DIR, 'config.json')
    else:
        # Home directory
        HOME       = os.environ['HOME']
        HOME       = os.path.join('/' , 'Users' , usr) if not HOME else HOME
        # Config directory
        CONFIG_DIR = os.path.join(HOME, '.config', 'markify')
        # Config file
        CONFIG_FP  = os.path.join(CONFIG_DIR, 'config.json')
    # Data directory
    DATA_DIR  = os.path.join(CONFIG_DIR, 'DATA')
    # Data file
    ct        = int(t.time()) # ct = current time
    DATA_FP   = os.path.join(DATA_DIR, f'{ct}.json')
    # Subsititutes the data file and config file if they're already given via CLI
    DATA_FP   = DATA_FP   if not args.data   else args.data
    CONFIG_FP = CONFIG_FP if not args.config else args.config
    # Returns everything
    return CONFIG_DIR, CONFIG_FP, DATA_DIR, DATA_FP






def f_time(seconds) -> str:
    """
    Convert a number of seconds into a string of the form `'Xhr Ymin Zsec'`. The function takes a single argument, `seconds`, and returns a string
    
    :param seconds: The number of seconds to convert to a string
    :return: A string with the time in hours, minutes, and seconds.
    """
    seconds = int(seconds)
    hr      = seconds // 3600
    min     = (seconds %  3600) // 60
    sec     = seconds  %  60

    res     = ''
    if hr:     res += f'{hr}hr '
    if min:    res += f'{min}min '
    if sec:    res += f'{sec}sec'
    return res





def f_disc_time(isoform: str):
    """
    Convert an ISO 8601 formatted string to a Unix timestamp
    
    :param isoform: str
    :type isoform: str
    :return: A string of the timestamp.
    """
    dt  = datetime.fromisoformat(isoform)
    ret = dt.timestamp()
    ret = int(ret)
    ret = str(ret)
    return ret










