from Megrendeles import Megrendeles
import regisztracio
import sorozat
import megrendelok


"""print("I/A, B:")
regisztracio.regisztracio()"""
sorozat.konzol_kiir()
sorozat.fajlba_ir(sorozat.nagyobb(sorozat.randomszam()))
sorok = megrendelok.beolvasas()
megrendelok.megrendelesek(sorok)
megrendelok.krumplifej(sorok)
megrendelok.utolso(sorok)