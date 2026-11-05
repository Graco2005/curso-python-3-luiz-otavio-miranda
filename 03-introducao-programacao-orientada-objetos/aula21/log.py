# Abstração

from pathlib import Path

LOG_FILE = Path(__file__).parent / "log.txt"

class Log():
  def _log(self, msg):
    raise NotImplementedError("Implemente o método log")

  def log_error(self, msg):
     return self._log(f"ERRO: {msg}")

  def log_sucess(self, msg):
     return self._log(f"SUCESSO: {msg}")

class LogFileMixin(Log):
    def _log(self, msg):
      msg_formatada = f"{msg} - {self.__class__.__name__}"
      print("Salvando no log: ", msg_formatada)
      with open(LOG_FILE, "a") as arquivo:
         arquivo.write(msg_formatada)
         arquivo.write("\n")

class LogPrintMixin(Log):
    def _log(self, msg):
      print(f"{msg} - {self.__class__.__name__}")

if __name__ == "__main__":
  lf = LogFileMixin()
  lf._log("Testando abstração das classes!")
  lf.log_error("Erro!")
  lf.log_sucess("Sucesso!")

  lp = LogPrintMixin()
  lp._log("Testando abstração das classes!")
  lp.log_error("Erro!")
  lp.log_sucess("Sucesso!")
  print(LOG_FILE)
