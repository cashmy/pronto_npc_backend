# users/serializers.py

from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

# Remove the top-level import:
# from referrals.models import Referral
from users.models import User


class CustomRegisterSerializer(RegisterSerializer):
    # Add additional fields you want from signup form
    referral_code = serializers.CharField(required=False, allow_blank=True)
    # company = serializers.CharField(required=False, allow_blank=True)

    def validate_referral_code(self, value):
        # Import here, only when validation runs
        from referrals.models import Referral

        if value:
            if not Referral.objects.filter(code=value).exists():
                raise serializers.ValidationError("Invalid referral code.")
        return value

    def custom_signup(self, request, user):
        # Import here, only when signup runs
        from referrals.models import Referral

        referral_code = self.validated_data.get("referral_code", None)
        # company = self.validated_data.get("company", None) # This seems commented out anyway

        # Ensure the profile exists before trying to modify it
        # (It might be created by a signal, but let's be safe)
        profile, created = user.profile.__class__.objects.get_or_create(user=user)

        # Save referral relationship
        if referral_code:
            # Use filter().first() to avoid DoesNotExist if code is validated but somehow gone
            referral = Referral.objects.filter(code=referral_code).first()
            if referral:
                # Check if the profile has a 'referred_by' field before assigning
                if hasattr(profile, "referred_by"):
                    # Check if the profile's referred_by field relates to the User model
                    # This assumes profile.referred_by is a ForeignKey to User
                    if (
                        profile._meta.get_field("referred_by").remote_field.model
                        == User
                    ):
                        profile.referred_by = referral.referred_by
                        profile.save()
                    else:
                        # Handle cases where referred_by might relate to something else
                        # or log a warning if the relationship is unexpected.
                        print(
                            f"Warning: Profile.referred_by does not relate to User model for user {user.id}"
                        )
                else:
                    # Handle cases where the profile model might not have 'referred_by'
                    # or log a warning.
                    print(
                        f"Warning: Profile model does not have a 'referred_by' field for user {user.id}"
                    )

        # # Save extra profile fields (Ensure profile exists first)
        # company = self.validated_data.get("company", None)
        # if company:
        #     if hasattr(profile, 'company'):
        #         profile.company = company
        #         profile.save()
        #     else:
        #          print(f"Warning: Profile model does not have a 'company' field for user {user.id}")

    # def get_cleaned_data(self): # This method seems incomplete/unused based on context
    #     # Override this to add extra fields you want saved
    #     data = super().get_cleaned_data()
    #     # data["company"] = self.validated_data.get("company", "") # 'company' isn't defined above
    #     return data


class OTPVerifySerializer(serializers.Serializer):
    otp = serializers.CharField(max_length=6)

    def validate_otp(self, value):
        if not value.isdigit() or len(value) != 6:
            raise serializers.ValidationError("OTP must be a 6-digit number.")
        return value
