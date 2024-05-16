from entity.Rating import Rating

class SubmitRatingController:

    def submitRatingController(self, receiver, sender, rating):
        rating_instance = Rating()
        submit_rating = rating_instance.submitRating(receiver, sender, rating)
        return submit_rating