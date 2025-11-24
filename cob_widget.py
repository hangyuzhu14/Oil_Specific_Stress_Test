from datetime import date, datetime, timedelta

from databricks.sdk.runtime import dbutils


class CoBWidget:
    def __init__(self) -> None:
        """
        Creates or connects a business date widget to the current Databricks environment. Can only be called from
        inside a Databricks workspace/cluster.
        """
        self._date_format = "%Y-%m-%d"
        self._widget_name = "businessDate"
        self._create_cob_widget()

    @property
    def date(self) -> str:
        """
        Access the date value of the widget business date.
        :return: Date string
        """
        return self._get_current_run_business_date()

    @property
    def day(self) -> int:
        """
        Access the day value of the widget business date.
        :return: Day integer
        """
        return self._current_run_day()

    @property
    def month(self) -> int:
        """
        Access the month value of the widget business date.
        :return: Month integer
        """
        return self._current_run_month()

    @property
    def year(self) -> int:
        """
        Access the year value of the widget business date.
        :return: Year integer
        """
        return self._current_run_year()

    def _get_current_run_business_date(self) -> str:
        """
        Return the current 7date set in the widget.
        :return: Widget date in string format
        """
        res: str = dbutils.widgets.get(self._widget_name)
        return res

    def _current_run_year(self) -> int:
        """
        Return the current year as an integer based on the currently set date in the widget.
        :return: Widget year as integer
        """
        run_cob = self._get_current_run_business_date()
        return datetime.strptime(run_cob, self._date_format).year

    def _current_run_month(self) -> int:
        """
        Return the current month as an integer based on the currently set date in the widget.
        :return: Widget month as integer
        """
        run_cob = self._get_current_run_business_date()
        return datetime.strptime(run_cob, self._date_format).month

    def _current_run_day(self) -> int:
        """
        Return the current day as an integer based on the currently set date in the widget.
        :return: Widget day as integer
        """
        run_cob = self._get_current_run_business_date()
        return datetime.strptime(run_cob, self._date_format).day

    def _create_cob_widget(self) -> None:
        """
        Create the default cob widget in Databricks.
        :return: None
        """
        today = date.today()
        if today.weekday() == 0:  # Monday
            result_date = today - timedelta(days=3)
        elif today.weekday() == 5:  # Saturday
            result_date = today - timedelta(days=1)
        elif today.weekday() == 6:  # Sunday
            result_date = today - timedelta(days=2)
        else:
            result_date = today - timedelta(days=1)

        dbutils.widgets.text("businessDate", result_date.strftime(self._date_format))
        run_cob = self._get_current_run_business_date()
        if not self._is_valid_past_or_current_cob_date(run_cob, date_format=self._date_format):
            raise Exception(
                f"Input business date ({run_cob}) is not a valid business date. CoB dates should be given as YYYY-MM-DD e.g. 2023-11-28 and should not fall on a weekend. Future dates will also be rejected."
            )

    @staticmethod
    def _is_valid_past_or_current_cob_date(date_string: str, date_format: str = "%Y-%m-%d") -> bool:
        """
        Validates the input date string to be a valid current or past date. Validity check fails
        on dates which can't be correctly parsed based on the input format.
        :param date_string: String representation of the date
        :param date_format: Format used for the string representation
        :return: Boolean. True if date is past or current. False otherwise.
        """
        try:
            date_object = datetime.strptime(date_string, date_format)
            if date_object.isoweekday() > 5:
                return False
            if date_object.date() > datetime.today().date():
                return False
        except ValueError:
            return False
        return True
