from resorts import verify_input
from message import carriers

def validate_args(args):
    if not verify_input(args.mountain):
        return False

    date = args.date.split('/')
    if (len(date) != 3 or len(date[0]) != 2 or len(date[1]) != 2 or len(date[2]) != 4
       or not date[0].isdigit() or not date[1].isdigit() or not date[2].isdigit()):
        return False

    if ((args.phone and not args.carrier) or (args.phone and not args.phone.isdigit())
       or (args.carrier and args.carrier not in carriers)):
        return False

    return True
