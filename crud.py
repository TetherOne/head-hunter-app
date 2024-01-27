import asyncio

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from core.models import db_helper, User, Profile, Resume


async def create_user(session: AsyncSession, username: str, surname: str):
    user = User(username=username, surname=surname)
    session.add(user)
    await session.commit()


async def get_user_by_username(session: AsyncSession, username: str) -> User | None:
    stmt = select(User).where(User.username == username)
    # result: Result = await session.execute(stmt)
    # # user: User | None = result.scalar_one_or_none()
    # user: User | None = result.scalar_one()
    user: User | None = await session.scalar(stmt)
    print("found user", username, user)
    return user


async def create_user_profile(
    session: AsyncSession,
    user_id: int,
    city: str | None = None,
    bio: str | None = None,
) -> Profile:
    profile = Profile(
        user_id=user_id,
        city=city,
        bio=bio,
    )
    session.add(profile)
    await session.commit()
    return profile


async def show_users_with_profiles(session: AsyncSession) -> list[User]:
    stmt = select(User).options(joinedload(User.profile)).order_by(User.id)
    users = await session.scalars(stmt)
    for user in users:
        print(user)
        if user.profile is not None:
            print(user.profile.bio)
        else:
            print("No profile for this user")


async def main():
    async with db_helper.session_factory() as session:
        # user_sam = await get_user_by_username(session=session, username='Sam')
        # await create_user_profile(
        #     session=session,
        #     user_id=user_sam.id,
        #     city='Loyrenc',
        #     bio='Люблю Руби')
        await show_users_with_profiles(session=session)


if __name__ == '__main__':
    asyncio.run(main())