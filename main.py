import flet as a

# main function
def main(page: a.Page):
    page.title = "BMI calculator "
    page.horizontal_alignment = a.MainAxisAlignment.START
   
    height_field = a.TextField(hint_text="Height (cm)")
    weight_field = a.TextField(hint_text="Weight (kg)")
    txt_number = a.TextField(value="", text_align=a.TextAlign.CENTER, width=100,hint_text="Age",)

    def calculate(age,weight,height):
        print(weight,height)
        if (age and weight and height):
            weight = int(weight)
            height= int(height)
            if ((height < 50 or height > 220) or (weight < 1 or weight > 300)):
                weight_field.border_color = a.Colors.RED_500
                height_field.border_color = a.Colors.RED_500
                weight_field.hint_text = '1 > weight < 300'
                height_field.hint_text = '50cm > height < 220cm'
                weight_field.value=""
                height_field.value=""

                page.update()
                return

            height = float(int(height)/100) # height in meters
            BMI = weight/(height**2)    
            print(BMI)
            if BMI< 18.5:
                page.controls.append(a.Text(f"You are underweight, your bmi is {round(BMI,2)}",color=a.Colors.RED_500,size=22,text_align=a.TextAlign.CENTER))
            elif BMI>=18.5 or BMI <24.9:
                page.controls.append(a.Text(f"you have healthy weight, your bmi is {round(BMI,2)}",color=a.Colors.GREEN_500,size=22,text_align=a.TextAlign.CENTER))
            elif BMI >=25 or BMI<29.9:
                page.controls.append(a.Text(f"you are over weight, your bmi is {round(BMI,2)}",color=a.Colors.RED_500,size=22,text_align=a.TextAlign.CENTER))
            else:
                page.controls.append(a.Text(f"obesity, your bmi is {round(BMI,2)}",color=a.Colors.RED_600,text_align=a.TextAlign.CENTER))
            page.update()
        else:
            print('else')
            txt_number.border_color=a.Colors.RED_400
            height_field.border_color=a.Colors.RED_400
            weight_field.border_color=a.Colors.RED_400

            txt_number.hint_text='required'
            txt_number.autofocus = True
            page.update()
            

    calc_btn = a.ElevatedButton(text="Calculate!",bgcolor='blue',color='white',width=100,on_click=lambda e: calculate(txt_number.value,weight_field.value,height_field.value))
    
    page.add(
        a.Row(
            [
                txt_number,
                height_field,
                weight_field,
                calc_btn
            ],
            alignment=a.MainAxisAlignment.CENTER,
        )
    )

a.app(main)
