from matplotlib_venn import venn2  
from matplotlib import pyplot as plt

# depict venn diagram 
venn2(subsets = (50, 10, 7), set_labels = ('Group A', 'Group B')) 
plt.title("Venn Diagram")   
plt.show()

# depict venn diagram without disproportionate sizes 
"""from matplotlib_venn import venn2_unweighted 
venn2_unweighted(subsets = (50, 10, 7), 
                 set_labels = ('Group A',  
                               'Group B'), 
                 set_colors=("orange", 
                             "blue"),alpha=0.7) 
plt.show()"""


# depict venn diagram with more defined lines for circles
"""from matplotlib_venn import venn2,venn2_circles 
venn2(subsets = (50, 10, 7), 
      set_labels = ('Group A',  
                    'Group B'), 
      set_colors=("orange", 
                  "blue"),alpha=0.7) 
  
# add outline 
venn2_circles(subsets=(50,10,7))  
plt.show()"""

# import modules 
from matplotlib_venn import venn2, venn2_circles 
from matplotlib import pyplot as plt 
  
# depict venn diagram with cricle outlines dashed - - - -
"""from matplotlib_venn import venn2, venn2_circles 
venn2(subsets=(50, 10, 7),  
      set_labels=('Group A', 'Group B'), 
      set_colors=("orange", "blue"), alpha=0.7) 
  
# outline of the circle with defined  
# line style and line width 
venn2_circles(subsets=(50, 10, 7),  
              linestyle="dashed", linewidth=2) 
plt.show() """



# 3 Circles Ven Diagram
"""from matplotlib_venn import venn3, venn3_circles 
from matplotlib import pyplot as plt 
  
# depict venn diagram 
venn3(subsets=(20, 10, 12, 10, 9, 4, 3),  
      set_labels=('Group A', 'Group B', 'Group C'),  
      set_colors=("orange", "blue", "red"), alpha=0.7) 
  
# outline of circle line style and width 
venn3_circles(subsets=(20, 10, 12, 10, 9, 4, 3), 
              linestyle="dashed", linewidth=2) 
  
# title of the venn diagram 
plt.title("Venn Diagram") 
plt.show() """