from wtforms import Form,SubmitField

class tech_data_operate(Form):
    openpage = SubmitField(label='打开成果库')
    down_scroll=SubmitField(label='下滚')
    up_scroll=SubmitField(label='上滚')
    tech_list = SubmitField(label='成果列表')
    tech_detail = SubmitField(label='成果详情')
    close = SubmitField(label='结束演示')


class main_guide(Form):
    openpage = SubmitField(label='打开成果库')
    down_scroll=SubmitField(label='下滚')
    up_scroll=SubmitField(label='上滚')
    tech_list = SubmitField(label='成果列表')
    tech_detail = SubmitField(label='成果详情')
    close = SubmitField(label='结束演示')
