print("First approach ")
import package2.module1
import package2.package3.module2

package2.module1.display()
package2.package3.module2.show()


print("second approach :")
from package2.module1 import *
from package2.package3.module2 import *
display()
show()
