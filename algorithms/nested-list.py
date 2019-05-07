marks = []
scorelist = []
if __name__ == '__main__':
        for _ in range(int(input())):
                name = input()
                score = float(input())
                marks.extend([[name,score]])
                scorelis.extend([score])
        b = sorted(list(set(scorelist)))[1] 
       

        for a,c in sorted(marks):
            if c == b:
                print(a)
