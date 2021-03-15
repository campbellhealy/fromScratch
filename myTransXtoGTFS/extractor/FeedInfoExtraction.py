File: Optional

The file contains information about the dataset itself, rather than the services that the dataset describes. Note that, in some cases, the publisher of the dataset is a different entity than any of the agencies.

Field Name	Type	Required	Description
feed_publisher_name	Text	Required	Full name of the organization that publishes the dataset. This may be the same as one of the agency.agency_name values.
feed_publisher_url	URL	Required	URL of the dataset publishing organization's website. This may be the same as one of the agency.agency_url values.
feed_lang	Language code	Required	Default language used for the text in this dataset. This setting helps GTFS consumers choose capitalization rules and other language-specific settings for the dataset.
feed_start_date	Date	Optional	The dataset provides complete and reliable schedule information for service in the period from the beginning of the feed_start_date day to the end of the feed_end_date day. Both days can be left empty if unavailable. The feed_end_date date must not precede the feed_start_date date if both are given. Dataset providers are encouraged to give schedule data outside this period to advise of likely future service, but dataset consumers should treat it mindful of its non-authoritative status. If feed_start_date or feed_end_date extend beyond the active calendar dates defined in calendar.txt and calendar_dates.txt, the dataset is making an explicit assertion that there is no service for dates within the feed_start_date to feed_end_date range but not included in the active calendar dates.
feed_end_date	Date	Optional	(see above)
feed_version	Text	Optional	String that indicates the current version of their GTFS dataset. GTFS-consuming applications can display this value to help dataset publishers determine whether the latest dataset has been incorporated.
feed_contact_email	Email	Optional	Email address for communication regarding the GTFS dataset and data publishing practices. feed_contact_email is a technical contact for GTFS-consuming applications. Provide customer service contact information through agency.txt.
feed_contact_url	URL	Optional	URL for contact information, a web-form, support desk, or other tools for communication regarding the GTFS dataset and data publishing practices. feed_contact_url is a technical contact for GTFS-consuming applications. Provide customer service contact information through agency.txt.