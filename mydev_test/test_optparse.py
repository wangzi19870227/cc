from optparse import OptionParser

def main():
    parser = OptionParser()
    parser.add_option(
        "-j", "--job",
        action="store",
        dest="job",
        type="choice",
        #default="dryrun",
        choices=['dryrun', 'billing', 'cboss', 'all'],
        help="valid job: dryrun, billing, cboss, all."
    )
    parser.add_option(
        "-r", "--region",
        action="store",
        dest="region",
        type="choice",
        #default="all",
        choices=['cn-north-1','ap-hongkong-1','us-east-1','us-west-1','all'],
        help="valid region: cn-north-1, ap-hongkong-1, us-east-1, us-west-1, all."
    )
    parser.add_option(
        "-t", "--resource_type",
        action="store",
        dest="resource_type",
        type="choice",
        #default="all",
        choices=['lcs_instance', 'lcs_volume', 'lcs_eip', 'l2b_lb', 'all'],
        help="valid resource type: lcs_instance, lcs_volume, lcs_eip, l2b_lb, all."
    )

    (options, args) = parser.parse_args()
    print('main(). options: %s, args: %s' % (options, args))

    job = options.job
    region = options.region
    resource_type = options.resource_type
    print('main(). job: %s, region: %s, resource_type: %s' % (job, region, resource_type))

    if job is None:
        print('not job spedifyed!')
        exit(1)
    if region is None:
        print('not region spedifyed!')
        exit(1)
    if resource_type is None:
        print('not resource type spedifyed!')
        exit(1)

main()
