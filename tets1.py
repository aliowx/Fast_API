import ezdxf


doc = ezdxf.readfile('/home/ali/Desktop/G1.dwg')

msp = doc.modelspace()

for entity in msp:
    print(entity.dxftype(), entity.dxf.handle)
