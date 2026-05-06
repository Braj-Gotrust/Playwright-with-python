
# and or element locate
save_review_msg = page.get_by_text(re.compile(r"Review saved successfully|Success!"))
expect(save_review_msg.first).to_be_visible(timeout=15000)

# visible
self.answers = page.locator("div[role='option']:visible")