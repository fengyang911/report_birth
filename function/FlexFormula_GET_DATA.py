class DynamicGetData(BaseFormulaObject):
    def do(self, day, data):
        current_date = self.context.get('CURRENT_DATE')
        year_month_list = current_date.split("-")
        _day, last_day = calendar.monthrange(int(year_month_list[0]), int(year_month_list[1]))
        if day > last_day:
            return ""
        else:
            return data