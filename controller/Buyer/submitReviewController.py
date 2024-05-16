from entity.Review import Review

class SubmitReviewController:

    def submitReviewController(self, receiver, sender, review):
        review_instance = Review()
        submit_review = review_instance.submitReview(receiver, sender, review)
        return submit_review