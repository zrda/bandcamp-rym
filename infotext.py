def contents():
    intro = "This tool enables you to retreive an album's Bandcamp tracklist in the correct format for submitting to the RateYourMusic database."
    step1 = "1) Enter the URL of your chosen album and click ^*Submit^"
    step2 = "2) After the tracklist has been formatted and displayed, click ^*Copy^"
    step3 = "3) Under ^*3.7 Track listing^ on the RYM Add Release page, click ^*Advanced^ and paste into the textarea that appears"
    step4 = "4) Click ^*Simple^ followed by ^*Preview your release submission^ at the bottom of the page to make sure the information is correct and adheres to the rules of capitalization"
    step5 = "5) Confirm that track lengths are correct. There is a bug in RYM that causes tracks of length 08:XX to be set to 00:00, so you may need to manually enter these as 8:XX after the previous step. I would be interested to know if this occurs for any other track lengths"
    outro = "I hope this can be of help to you! If you encounter any errors or have a suggestion, you can contact me ^@here^"

    return [step.split('^') for step in [intro, step1, step2, step3, step4, step5, outro]]