"""Worked learning example for day 065; independent of the exercises."""

def main():
    import logging
    logger = logging.getLogger("lesson")
    handler = logging.StreamHandler()
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    logger.info("processed %s records", 3)


if __name__ == "__main__":
    main()
