from notifypy import Notify


def notify_user(title: str, message: str):
    notification = Notify()
    notification.title = title
    notification.message = message
    notification.send()
