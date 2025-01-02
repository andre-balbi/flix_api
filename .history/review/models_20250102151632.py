from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
    movie = (
        models.ForeignKey(
            "movies.Movie", on_delete=models.PROTECT, related_name="reviews"
        ),
    )
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0, "Minimum value is 0"),
            MaxValueValidator(5, "Maximum value is 5"),
        ]
    )
    comment = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):
        # For movie, use a foreign key, so the __str__ method of this model should look like this `self.movie`
        return f"{self.movie} - {self.stars}"
