#!usr/bin/env python3

import logging

logging.basicConfig(
    filename= "app.log",
    level= logging.DEBUG,
    format="%(asctime)s [ %(levelname)s ] %(name)s\n" +
       "[ %(funcName)s ] [ %(filename)s, %(lineno)s ] %(message)s",
    datefmt= "[ %d/%m/%Y %H:%M:%S ]" 
)

# Loglevel INFO 
# logging.info("Mensagem de teste")

# Loglevel customizado
CUSTOM = 49
logging.addLevelName(CUSTOM, "CUSTOM")
def custom(self, message, *args, **kwargs):
    if self.isEnabledFor(CUSTOM):
        self._log(CUSTOM, message, args, **kwargs)
logging.Logger.custom = custom
logger = logging.getLogger()
logger.custom("Meu log customizado")