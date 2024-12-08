from Graphics import rectangle as r
from Graphics import circle as c
from Graphics.graphics3D import cuboid as cb
from Graphics.graphics3D import sphere as s


def p():
 print("----------------------------------------------------------------------------------------------------")

while(True):
 choice=int(input("select Geometric shape:\n1.rectangle\n2.circle\n3.cuboid\n4.sphere\n5.exit\n:::: "))
 if(choice==1):
  p()
  l=int(input("\nLength: "))
  w=int(input("\nwidth: "))
  print("\nArea: ",r.area(l,w))
  print("\nPerimeter: ",r.perimeter(l,w))
  p()
 elif(choice==2):
  p()
  r=int(input("\nRadius: "))
  print("\nArea",c.area(r))
  p()
 elif(choice==3):
  p()
  l=int(input("\nLength: "))
  w=int(input("\nwidth: "))
  h=int(input("\nheight: "))
  print("\nArea: ",cb.area(l,w,h))
  print("\nVolume: ",cb.volume(l,w,h))
  p()
 elif(choice==4):
  p()
  r=int(input("\nRadius: "))
  print("\nArea",s.area(r))
  print("\nVolume:",s.volume(r))
  p()

 elif(choice==5):
     break;
 elif(choice not in [1,2,3,4,5]):
  p()
  print("Invalid choice")
  p()
