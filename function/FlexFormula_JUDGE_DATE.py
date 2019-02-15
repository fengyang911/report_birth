class DynamicGetDate(BaseFormulaObject):
    """判断当前时间是否存在"""
    def do(self, day):
        year_month_list = self.context.get('CURRENT_DATE')
        year = year_month_list.split("-")[0]
        month = year_month_list.split("-")[1]
        w_day, last_day = calendar.monthrange(int(year), int(month))
        if int(day) > last_day:
            return ""
        else:
            return str(day) + "号"