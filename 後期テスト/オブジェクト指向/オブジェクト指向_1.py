class Student:
    def __init__(self,name,weight,height):
        self.name = name 
        self._weight = weight
        self._height = height
    def sindan(self):
        print(f'{self.name}さん、身長：{self._height},体重：{self._weight}')
    

student1 = Student('鈴木',70,166)
student1.sindan()
student2 = Student('佐藤',56,154)
student2.sindan()

class Sika(Student):
    def __init__(self, name,weight,height,sikakensin,zibyou):
        super().__init__(name,weight,height)
        self.sikakensin = sikakensin
        self.zibyou = zibyou
    def sindan(self):
        print(f'{self.name}さん、身長:{self._height}cm、',end='')
        print(f'体重:{self._weight}kg、{self.sikakensin}、{self.zibyou}')
student3 = Sika("田中",75,175,'虫歯なし','持病なし')
student3.sindan() 
student3 = Sika("斉藤",70,160,"虫歯あり",'持病なし')
student3.sindan()